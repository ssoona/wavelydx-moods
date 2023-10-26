# wavelydx-moods
Backend engineer hiring assessment for WavelyDx

## Architecture
S3
- Object storage best suited for audio files.
- Structured to have a folder for each mood type. Service code enforces that only one audio file for each mood can exist at a time.
- Policy enforcing that only .mp3/.wav files can be uploaded in place.
Lambda
- Used to host the service code
- Chosen for simplicity in deploying/testing

Further components I would want to add
- Caching/CDN
- AWS SDK/Cloudformation for infrastructure provisioning
