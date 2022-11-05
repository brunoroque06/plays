#!/usr/bin/env elvish

use path

git clone --depth 1 https://github.com/brunoroque06/plays.git

cd plays
git rm '*'

cd ..
git ls-files ^
  | from-lines ^
  | each { |file|
    var f = (path:join plays $file)
    var d = (path:dir $f)
    mkdir -p $d
    cp $file $f
  }

cd plays
git checkout -b zazu
git add -A
git commit -m 'Release'
git push --force origin zazu

cd ..
rm -fr plays
