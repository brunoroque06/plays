#!/usr/bin/env elvish

use path

git clone --depth 1 https://github.com/brunoroque06/playground.git

cd playground
git rm '*'

cd ..
git ls-files ^
  | from-lines ^
  | each { |src|
    var f = (path:join playground $src)
    var d = (path:dir $f)
    mkdir -p $d
    cp $src $f
  }

cd playground
git checkout -b zazu
git add -A
git commit -m 'Add zazu'
git push --force origin zazu

cd ..
rm -fr playground
