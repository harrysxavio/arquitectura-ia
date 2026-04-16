# Constraints

> Compact constraints for the SAMPLE_PROJECT support desk example.

## Technical

- Do not turn the sample into a production app.
- Do not add runtime dependencies for the mini app.
- Keep code small and aligned with OpenSpec.
- Do not treat runtime JSON as canonical.
- Do not treat Graphify output as a source of truth.

## Business

- Cover only internal operations support requests.
- Do not model external customer support.
- Do not store real person, customer or incident data.

## Security

- Do not store credentials, tokens or secrets in Markdown.
- `.env.example` may contain dummy variable names only.

## Cost

- Do not add paid services or hosting.
