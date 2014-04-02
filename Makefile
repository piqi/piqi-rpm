# upstream version
VERSION = 0.6.6
COMMIT = ded745779a8216b838302e1e1ae4e5f5adacd3b0


# extracting download URL from .spec works only for rpm-4.11.0 and higher
# versions; previous versions of rpmspec require source to be already present
#DOWNLOAD_URL := $(shell rpmspec -P piqi.spec | grep '^Source0:' | cut -f 2)
SHORTCOMMIT  := $(shell echo $(COMMIT) | cut -c 1-7)
DOWNLOAD_URL := https://github.com/alavrik/piqi/archive/$(COMMIT)/piqi-$(VERSION)-$(SHORTCOMMIT).tar.gz

TARBALL      := $(notdir $(DOWNLOAD_URL))


RPMBUILDFLAGS = \
	--define "_topdir $(PWD)" \
	#--nodeps


all: download rpm


download: $(TARBALL)


$(TARBALL):
	curl -L -O $(DOWNLOAD_URL)


rpm: download clean-rpm
	mkdir SOURCES && cp $(TARBALL) SOURCES
	rpmbuild -ba $(RPMBUILDFLAGS) piqi.spec


clean: clean-rpm
	rm -rf piqi-*.tar.gz


clean-rpm:
	#rpmbuild --clean $(RPMBUILDFLAGS) piqi.spec
	rm -rf BUILD RPMS SOURCES SPECS SRPMS BUILDROOT


.PHONY: all download rpm clean clean-rpm
