FROM alpine:latest
RUN apk add --no-cache curl
COPY config.txt /app/config.txt
CMD ["cat", "/app/config.txt"]
