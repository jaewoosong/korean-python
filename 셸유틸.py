import os
import shutil

# 각 단원 내에서 함수는 가나다순으로 정렬되어 있습니다.

#-------------------------------
# 11.10.1. 디렉토리 및 파일 작업
#-------------------------------

def 복사(src, dst, *, follow_symlinks=True):
    return shutil.copy(src, dst, follow_symlinks=follow_symlinks)

def 복사2(src, dst, *, follow_symlinks=True):
    return shutil.copy2(src, dst, follow_symlinks=follow_symlinks)

def 접근권한복사(src, dst, *, follow_symlinks=True):
    return shutil.copymode(src, dst, follow_symlinks=follow_symlinks)

def 파일객체복사(fsrc, fdst, length=16*1024):
    return shutil.copyfileobj(fsrc, fdst, length)

def 파일복사(src, dst, *, follow_symlinks=True):
    return shutil.copyfile(src, dst, follow_symlinks=follow_symlinks)

def 파일상태복사(src, dst, *, follow_symlinks=True):
    return shutil.copystat(src, dst, follow_symlinks=follow_symlinks)

def 디렉토리복사(src, dst, symlinks=False, ignore=None,
                 copy_function=shutil.copy2, ignore_dangling_symlinks=False):
    return copytree(src, dst, symlinks=symlinks, ignore=ignore,
                    copy_function=copy_function,
                    ignore_dangling_symlinks=ignore_dangling_symlinks)

def 디렉토리삭제(path, ignore_errors=False, onerror=None):
    # rmtree.avoids_symlink_attacks
    return shutil.rmtree(path, ignore_errors=ignore_errors, onerror=onerror)

def 이동(src, dst, copy_function=shutil.copy2):
    return shutil.move(src, dst, copy_function=copy_function)

# shutil.ignore_patterns(*patterns)
# This factory function creates a function that can be used as a callable for copytree()‘s ignore argument, ignoring files and directories that match one of the glob-style patterns provided. See the example below.

def 디스크사용량(path):
    return shutil.disk_usage(path)

def 소유권변경(path, user=None, group=None):
    return shutil.chown(path, user=user, group=group)

def 어디(cmd, mode=os.F_OK | os.X_OK, path=None):
    return shutil.which(cmd, mode=mode, path=path)

#exception shutil.Error


#------------------------
# 11.10.2. 압축 파일 작업
#------------------------


'''
11.10.2. Archiving operations
New in version 3.2.

Changed in version 3.5: Added support for the xztar format.

High-level utilities to create and read compressed and archived files are also provided. They rely on the zipfile and tarfile modules.

shutil.make_archive(base_name, format[, root_dir[, base_dir[, verbose[, dry_run[, owner[, group[, logger]]]]]]])
Create an archive file (such as zip or tar) and return its name.

base_name is the name of the file to create, including the path, minus any format-specific extension. format is the archive format: one of “zip” (if the zlib module is available), “tar”, “gztar” (if the zlib module is available), “bztar” (if the bz2 module is available), or “xztar” (if the lzma module is available).

root_dir is a directory that will be the root directory of the archive; for example, we typically chdir into root_dir before creating the archive.

base_dir is the directory where we start archiving from; i.e. base_dir will be the common prefix of all files and directories in the archive.

root_dir and base_dir both default to the current directory.

If dry_run is true, no archive is created, but the operations that would be executed are logged to logger.

owner and group are used when creating a tar archive. By default, uses the current owner and group.

logger must be an object compatible with PEP 282, usually an instance of logging.Logger.

The verbose argument is unused and deprecated.

shutil.get_archive_formats()
Return a list of supported formats for archiving. Each element of the returned sequence is a tuple (name, description).

By default shutil provides these formats:

zip: ZIP file (if the zlib module is available).
tar: uncompressed tar file.
gztar: gzip’ed tar-file (if the zlib module is available).
bztar: bzip2’ed tar-file (if the bz2 module is available).
xztar: xz’ed tar-file (if the lzma module is available).
You can register new formats or provide your own archiver for any existing formats, by using register_archive_format().

shutil.register_archive_format(name, function[, extra_args[, description]])
Register an archiver for the format name.

function is the callable that will be used to unpack archives. The callable will receive the base_name of the file to create, followed by the base_dir (which defaults to os.curdir) to start archiving from. Further arguments are passed as keyword arguments: owner, group, dry_run and logger (as passed in make_archive()).

If given, extra_args is a sequence of (name, value) pairs that will be used as extra keywords arguments when the archiver callable is used.

description is used by get_archive_formats() which returns the list of archivers. Defaults to an empty string.

shutil.unregister_archive_format(name)
Remove the archive format name from the list of supported formats.

shutil.unpack_archive(filename[, extract_dir[, format]])
Unpack an archive. filename is the full path of the archive.

extract_dir is the name of the target directory where the archive is unpacked. If not provided, the current working directory is used.

format is the archive format: one of “zip”, “tar”, “gztar”, “bztar”, or “xztar”. Or any other format registered with register_unpack_format(). If not provided, unpack_archive() will use the archive file name extension and see if an unpacker was registered for that extension. In case none is found, a ValueError is raised.

shutil.register_unpack_format(name, extensions, function[, extra_args[, description]])
Registers an unpack format. name is the name of the format and extensions is a list of extensions corresponding to the format, like .zip for Zip files.

function is the callable that will be used to unpack archives. The callable will receive the path of the archive, followed by the directory the archive must be extracted to.

When provided, extra_args is a sequence of (name, value) tuples that will be passed as keywords arguments to the callable.

description can be provided to describe the format, and will be returned by the get_unpack_formats() function.

shutil.unregister_unpack_format(name)
Unregister an unpack format. name is the name of the format.

shutil.get_unpack_formats()
Return a list of all registered formats for unpacking. Each element of the returned sequence is a tuple (name, extensions, description).

By default shutil provides these formats:

zip: ZIP file (unpacking compressed files works only if the corresponding module is available).
tar: uncompressed tar file.
gztar: gzip’ed tar-file (if the zlib module is available).
bztar: bzip2’ed tar-file (if the bz2 module is available).
xztar: xz’ed tar-file (if the lzma module is available).
You can register new formats or provide your own unpacker for any existing formats, by using register_unpack_format().

11.10.2.1. Archiving example
In this example, we create a gzip’ed tar-file archive containing all files found in the .ssh directory of the user:

>>>
>>> from shutil import make_archive
>>> import os
>>> archive_name = os.path.expanduser(os.path.join('~', 'myarchive'))
>>> root_dir = os.path.expanduser(os.path.join('~', '.ssh'))
>>> make_archive(archive_name, 'gztar', root_dir)
'/Users/tarek/myarchive.tar.gz'
The resulting archive contains:

$ tar -tzvf /Users/tarek/myarchive.tar.gz
drwx------ tarek/staff       0 2010-02-01 16:23:40 ./
-rw-r--r-- tarek/staff     609 2008-06-09 13:26:54 ./authorized_keys
-rwxr-xr-x tarek/staff      65 2008-06-09 13:26:54 ./config
-rwx------ tarek/staff     668 2008-06-09 13:26:54 ./id_dsa
-rwxr-xr-x tarek/staff     609 2008-06-09 13:26:54 ./id_dsa.pub
-rw------- tarek/staff    1675 2008-06-09 13:26:54 ./id_rsa
-rw-r--r-- tarek/staff     397 2008-06-09 13:26:54 ./id_rsa.pub
-rw-r--r-- tarek/staff   37192 2010-02-06 18:23:10 ./known_hosts
'''


#--------------------
# 11.10.3. 
#--------------------

'''
11.10.3. Querying the size of the output terminal
shutil.get_terminal_size(fallback=(columns, lines))
Get the size of the terminal window.

For each of the two dimensions, the environment variable, COLUMNS and LINES respectively, is checked. If the variable is defined and the value is a positive integer, it is used.

When COLUMNS or LINES is not defined, which is the common case, the terminal connected to sys.__stdout__ is queried by invoking os.get_terminal_size().

If the terminal size cannot be successfully queried, either because the system doesn’t support querying, or because we are not connected to a terminal, the value given in fallback parameter is used. fallback defaults to (80, 24) which is the default size used by many terminal emulators.

The value returned is a named tuple of type os.terminal_size.

See also: The Single UNIX Specification, Version 2, Other Environment Variables.

New in version 3.3.

'''
