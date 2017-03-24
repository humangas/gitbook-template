# -*- coding: utf-8 -*-

import shutil
import os
import hashlib


def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        for filen in files:
            yield filen

# TODO: FAQ用になってるので、これをディレクトリ名/xx.mdの形にも対応させるとともに、リンクはhashで作り出す。NFC対策
# mkdocsex 実装を取り込む（汎用的なつくりにする）
# -> target（docはいってるフォルダ）= assets の中身をコピー -> buildへ
# build の中身のファイルをmd5で名前にして、リンクを差し替える 
# フォルダ名をサマリの項目にする
def main():
    asstesdir = 'assets'
    builddir = 'build'
    summaryfile = 'SUMMARY.md'

    shutil.rmtree(builddir)
    shutil.copytree(asstesdir, builddir)

    summarymd = []
    summarymd.append('# Summary\n\n')
    category_dict = {}

    for filen in find_all_files(builddir):
        category = filen.split('-', 1)[0]
        file_path = '{0}/{1}'.format(builddir, hashlib.md5(filen).hexdigest())

        title = []
        for tag in filen.split('-'):
            title.append('\[{}\]'.format(tag))
        title[-1] = tag
        titlestr = ' '.join(title)
        root, ext = os.path.splitext(titlestr)
        src_filepath = '{0}/{1}'.format(builddir, filen)
        dst_filepath = '{0}{1}'.format(file_path, ext)
        shutil.move(src_filepath, dst_filepath)
        index = '- [{0}]({1})\n'.format(root, dst_filepath)

        if category in category_dict:
            titles = category_dict[category]
            titles.append(index)
        else:
            titles = []
            titles.append(index)
            category_dict[category] = titles

    for k, vs in category_dict.items():
        summarymd.append('## {}\n'.format(k))
        for v in vs:
            summarymd.append(v)
        summarymd.append('\n')

    with open(summaryfile, 'w') as f:
        f.writelines(summarymd)


if __name__ == '__main__':
    main()
