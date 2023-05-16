

#### Build

```bash
docker buildx build --push \
--tag ghcr.io/ckam225/university-master-client \
--build-arg API_URL=http://185.213.209.163:9001 \
--platform=linux/arm64,linux/amd64 .

# 0R FOR LOCAL
docker buildx build --push \
--tag ghcr.io/ckam225/university-master-client \
--build-arg API_URL=http://localhost:8000 \
--platform=linux/arm64,linux/amd64 .
```

#### Run
```bash
docker run --rm -it --name master-faces -p 9000:80 ghcr.io/ckam225/university-master-client:latest
```