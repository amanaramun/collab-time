# Installation process
## Install Git Bash for windows
1. https://gitforwindows.org/
2. one of the options is to "install with NEW feature changing master to main" click that one because all the future instructions refrence main instead of master
3. i randomlly clicked stuff, like fast-foard or merging
4. Optional Install VS code
a. https://code.visualstudio.com/download
## git terminal in VS code v.s. GitBash
<ol>
<li>Create your working windows folder</li>
<li>in VS code you can use the "open folder" option </li>
<ol>
<li>hit
                ctrl+~
to bring up the terminal</li>
<li>bottom right hand corner you'll see powershell</li>
<li> next to it you'll see a +, click it and add git bash</li>
<li> click bash, you'll see in the terminal "username" MINGH64/ "dir" main  git terminal should be set up, if not type in `git init`</li>
</ol>
</li>
<li>Git bash</li>
<ol>
<ls> In the directory you made, right click,right click, 

                more options,

                open git bash here

 (i dont know how to use the gui)
</ol>


## Git Init

<li> set up user name and email </li>

<li> type in 

                ```bash
                git config --user.name "your name"
                git config --user.email "your email"

                ```

</li>

<li> type in 

                git config --user.name "your name" 

</li>

<li>provide me with user name and i'll add you to the repository </li>

## Once you're added

<li> I just used HTML, you'll see on the collab-time repo  /<>code icon, click that, and get the url </li>
<li>in your bash terminal type in </li>
            
            git remote add origin https://github.com/amanaramun/collab-time.git

<ol>            
<li> if you get an remote: Invalid username or password. fatal: Authentication failed,  see https://stackoverflow.com/questions/40957380/remote-invalid-username-or-password-fatal-authentication-failed </li>
<li> add git hub generic credential with your username and password </li>
</ol>

<li> for the first time pulling you need to use the syntax

                git pull origin main

 (origin is the default branch name on the github repo) ( is your local main branch this is why we used the NEW to install master to main) </li>

 <li> subsquent pulls you canjust use 

                git pull

</li>
