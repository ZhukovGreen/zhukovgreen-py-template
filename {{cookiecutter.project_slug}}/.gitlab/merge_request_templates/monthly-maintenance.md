<!-- Thank you for your contribution!

Specify here the list of referenced issues and issues, which are going to
be closed by this MR

i.e.

Ref # XXX

Ref # XXX

Closes # XXX

Closes # XXX

-->

# Checklist

- [ ] Source branch name is chore/monthly-maintenance/{month: str}-{year: int}
- [ ] Check for update the python dependencies and pre-commit config
      (run `make bump_dependencies`)
- [ ] Check for updates in docker-compose version https://gitlab.cee.redhat.com/oamg/hardware-support-removal/-/blob/develop/docker-compose.yml#L1
- [ ] Check for updates in python version and if there is a new one, then update:
    - [ ] https://gitlab.cee.redhat.com/oamg/hardware-support-removal/-/blob/develop/.gitlab-cee-ci.yml#L1
    - [ ] https://gitlab.cee.redhat.com/oamg/hardware-support-removal/-/blob/develop/Dockerfile#L2
- [ ] Check if a newer version of poetry is available and bump it here:
https://gitlab.cee.redhat.com/oamg/hardware-support-removal/-/blob/develop/Dockerfile#L16
- [ ] Bump the version of the package in `pyproject.toml["tool.poetry"]["version"]`
- [ ] Fastforward master branch
- [ ] Update CHANGELOG.md with all changes which were added to master
- [ ] Resolve the relevant issue for this maintenance and create an issue for
      the next maintenance  with the due date in the end of the first week of
      the next month
