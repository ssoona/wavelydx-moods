# wavelydx-moods
Backend engineer hiring assessment for WavelyDx

## Architecture
### S3
- Object storage best suited for audio files.
- Structured to have a folder for each mood type. Service code enforces that only one audio file for each mood can exist at a time.
- Policy enforcing that only .mp3/.wav files can be uploaded in place.
### Lambda
- Used to host the service code
- Chosen for simplicity in deploying/testing
### CloudFormation
- Built in logging
### Diagram
![architecture diagram](http://github.com/ssoona/wavelydx-moods/blob/main/service_architecture.png?raw=true)

## Further components to add
- Define a proper API (API Gateway)
- Caching/CDN (CloudFront)
- AWS SDK/Cloudformation for infrastructure provisioning
