A=family.tar
PYTHON=python
PY_MANAGE=$(PYTHON) manage.py

VERSION:
	git describe > VERSION

dist: VERSION
	git archive -o $(A) HEAD
	tar -rf $(A) VERSION
	gzip -f $(A)

deploy: deploy_static
	$(PY_MANAGE) collectstatic -l --noinput
	$(PY_MANAGE) migrate
	$(PY_MANAGE) compilemessages

deploy_static:
	$(MAKE) PATH=$(PATH) -C $(CURDIR) deploy_static.worker

deploy_static.worker:
	cd core/static && bower install --allow-root


.PHONY: VERSION