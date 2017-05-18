make-caches:
	@ echo -n "[INFO] Creation " && \
		docker volume create alpine3.4-apk-cache
	@ echo -n "[INFO] Creation " && \
		docker volume create alpine3.5-apk-cache


# Based on https://docs.docker.com/engine/tutorials/dockervolumes/#backup-restore-or-migrate-data-volumes
backup-caches:
	@ echo "[INFO] Backup Alpine 3.4 cache" && \
	docker run --rm \
		--volume alpine3.4-apk-cache:/etc/apk/cache \
		--volume $(shell pwd)/backup:/backup \
		alpine:3.4 \
		tar cvf /backup/alpine3.4-apk-cache.backup.tar /etc/apk/cache
	@ echo "[INFO] Backup Alpine 3.5 cache" && \
	docker run --rm \
		--volume alpine3.5-apk-cache:/etc/apk/cache \
		--volume $(shell pwd)/backup:/backup \
		alpine:3.5 \
		tar cvf /backup/alpine3.5-apk-cache.backup.tar /etc/apk/cache

# Based on https://docs.docker.com/engine/tutorials/dockervolumes/#backup-restore-or-migrate-data-volumes
restore-caches:
	@ echo "[INFO] Restore Alpine 3.4 cache" && \
	docker run --rm \
		--volume alpine3.4-apk-cache:/etc/apk/cache \
		--volume $(shell pwd)/backup:/backup \
		alpine:3.4 \
		tar xvf /backup/alpine3.4-apk-cache.backup.tar
	@ echo "[INFO] Restore Alpine 3.5 cache" && \
	docker run --rm \
		--volume alpine3.5-apk-cache:/etc/apk/cache \
		--volume $(shell pwd)/backup:/backup \
		alpine:3.5 \
		tar xvf /backup/alpine3.5-apk-cache.backup.tar
