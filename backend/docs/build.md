

#### Build

```bash
docker buildx build --push \
--tag ghcr.io/ckam225/university-master-server \
--platform=linux/arm64,linux/amd64 .


#### Run
```bash
docker run --rm -it --name master-faces-server -p 9001:8000 ghcr.io/ckam225/university-master-server:latest
```