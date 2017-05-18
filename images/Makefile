MAKEFILE := $(lastword $(MAKEFILE_LIST))

alpine3.5:
	/media/d2/dev/github/docker-image-builder/target/docker-image-builder build \
		-s alpine:3.5 \
		-t ownport/alpine3.5:201705v1 \
		--build-modules-path $(shell pwd) \
		--build-module buildmodules.alpine.v1 \
		--re-run \
		--remove-staging \
		--volume alpine3.5-apk-cache:/etc/apk/cache/ \
		--vars $(shell pwd)/etc/buildmodules.yaml

alpine3.5-apkcache:
	/media/d2/dev/github/docker-image-builder/target/docker-image-builder build \
		-s alpine:3.5 \
		-t ownport/alpine3.5-apkcache:201705v1 \
		--build-modules-path $(shell pwd) \
		--build-module buildmodules.alpine.v1.apkcache \
		--re-run \
		--remove-staging \
		--volume alpine3.5-apk-cache:/etc/apk/cache/ \
		--vars $(shell pwd)/etc/buildmodules.yaml

alpine3.5-py2.7:
	/media/d2/dev/github/docker-image-builder/target/docker-image-builder build \
		-s alpine:3.5 \
		-t ownport/alpine3.5-py2.7:201705v1 \
		--build-modules-path $(shell pwd) \
		--build-module buildmodules.alpine.v1.python \
		--re-run \
		--remove-staging \
		--volume alpine3.5-apk-cache:/etc/apk/cache/ \
		--vars $(shell pwd)/etc/buildmodules.yaml

alpine3.5-py3.5:
	/media/d2/dev/github/docker-image-builder/target/docker-image-builder build \
		-s alpine:3.5 \
		-t ownport/alpine3.5-py3.5:201705v1 \
		--build-modules-path $(shell pwd) \
		--build-module buildmodules.alpine.v1.python3 \
		--re-run \
		--remove-staging \
		--volume alpine3.5-apk-cache:/etc/apk/cache/ \
		--vars $(shell pwd)/etc/buildmodules.yaml

build-all: \
	alpine3.5 \
	alpine3.5-apkcache \
	alpine3.5-py2.7 \
	alpine3.5-py3.5
