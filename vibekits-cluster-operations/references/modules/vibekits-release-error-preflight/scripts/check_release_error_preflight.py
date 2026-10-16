#!/usr/bin/env python3
"""Reject missing/stale VibeKits historical-regression evidence; not a test runner."""
import hashlib
import json
from pathlib import Path
import sys

COMMON = (
    'source-inputs', 'version-identity', 'package-completeness', 'runtime-functions',
    'upgrade-continuity', 'routing-auth-identity', 'startup-single-instance', 'simulation-reentry',
    'credential-replacement', 'truthful-status', 'session-lifecycle',
    'resource-lifecycle', 'market-install', 'evidence-integrity', 'delivery-cleanup',
)
PLATFORM = {
    'pad': ('pad-native-helper', 'pad-input-display'),
    'macos': ('mac-signing-loader', 'mac-first-input'),
    'windows': ('windows-package-updater', 'windows-permission-ui'),
}

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

def check(receipt_path):
    receipt_path = Path(receipt_path).resolve()
    data = json.loads(receipt_path.read_text())
    artifact = data['artifact']
    platform = artifact['platform']
    if platform not in PLATFORM:
        raise ValueError('unsupported_platform')
    path = Path(artifact['path'])
    if not path.is_absolute() or not path.is_file():
        raise ValueError('artifact_missing_or_not_absolute')
    sha = digest(path)
    if artifact['sha256'] != sha or artifact['bytes'] != path.stat().st_size:
        raise ValueError('artifact_identity_mismatch')
    if not artifact.get('version') or not isinstance(artifact.get('build'), int) or artifact['build'] < 1:
        raise ValueError('version_identity_missing')
    phase = data.get('phase')
    if phase not in {'prepublish', 'delivery'}:
        raise ValueError('release_phase_missing')
    required = COMMON + PLATFORM[platform]
    if phase == 'prepublish':
        required = tuple(case for case in required if case != 'delivery-cleanup')
    rows = data.get('results', [])
    results = {}
    for row in rows:
        if row['id'] in results:
            raise ValueError('duplicate_result')
        results[row['id']] = row
    failures = []
    for case in required:
        row = results.get(case)
        if not row or row.get('status') != 'pass' or row.get('artifactSha256') != sha:
            failures.append(case + ':missing_failed_or_stale')
            continue
        evidence = row.get('evidence')
        if not isinstance(evidence, list) or not evidence:
            failures.append(case + ':missing_evidence')
            continue
        for item in evidence:
            proof = Path(item.get('path', ''))
            if not proof.is_absolute():
                proof = receipt_path.parent / proof
            if not proof.is_file() or proof.resolve() in {receipt_path, path.resolve()} or digest(proof) != item.get('sha256'):
                failures.append(case + ':evidence_identity_mismatch')
    if failures:
        return {'decision': 'BLOCK', 'failures': failures}
    return {'decision': 'PASS', 'scope': 'evidence_integrity_only',
            'functionalPassRequiresExistingReleaseGates': True, 'artifactSha256': sha,
            'phase': phase, 'caseCount': len(required)}

if __name__ == '__main__':
    try:
        result = check(sys.argv[1])
    except (IndexError, KeyError, TypeError, ValueError, OSError) as error:
        result = {'decision': 'BLOCK', 'reason': type(error).__name__}
    print(json.dumps(result, ensure_ascii=False))
    sys.exit(0 if result['decision'] == 'PASS' else 1)
