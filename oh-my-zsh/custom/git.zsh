git_add_modified() {
  for i in `git status | grep modified | awk '{print $2}'`
  do
    echo $i
    git add $i
  done
}

alias gh='cd $HOME/git'
alias gam='git_add_modified'
alias gbw='git branch working'
alias gcm='git checkout master'
alias gcw='git checkout working'
alias gmm='git merge master'
alias gmw='git merge working'
alias gca='git commit -C HEAD --amend'
alias grh='git reset --hard HEAD'

