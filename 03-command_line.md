# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> >   
- **pushd**     : "pushes" the current directory into a list for later, then it changes to the directory specified.  
- **popd**      : "pops" off the last directory you are at and returns you back to the directory from which you last "pushd".  
- **mkdir -p**  : makes an entire path even if all the directories do not exist (yet).  
- **CTRL Y**    : Paste  
- **cp -R [stuff] [otherStuff]**    : copy (from) and rename a folder  
- **cp *.txt stuff/**   : copy all of *[file type] to folder  
- **rm -i [file] ..**   : ask for confirmation each file  
- **rm -f [fileName]**      : force deletion of a file  
- **touch [fileName]**      : create or update a file  
- **find -name “*text”**    : search for files that ends with the word text  
- **grep -r [text] [folderName]/**    : search for file names with occurrence of the text  
  
> > ref http://cli.learncodethehardway.org/bash_cheat_sheet.pdf

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`		
`ls -a`		
`ls -l`		
`ls -lh`	
`ls -lah`  	
`ls -t`  	
`ls -Glp`  	

> > 
- `ls`		: lists all files in the directory that match the name. If name is left blank, it will list all of the files in the directory  
- `ls -a`		: lists all files in current folder including '.'  
- `ls -l`		: shows the long format listing of files in current folder  
- `ls -lh`	: use human readable format for sizes in the long format listing of current folder  
- `ls -lah`  	: shows using human readable format for sizes in the long format listing of all files in current folder  
- `ls -t`  	: list files in directory, sorting by modification time  
- `ls -Glp`  	: shows long format listing of files in current folder, highlighting those that are directories by appending the "/" indicator to directories.  

> > 
####Helpful References: 
- http://www.techonthenet.com/unix/basic/ls.php 
- http://linuxcommand.org/man_pages/ls1.html   
- http://man7.org/linux/man-pages/man1/ls.1.html  


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> >   
-c	 : Displays files by file timestamp.  
-d	 :	Displays only directories.  
-F	 :	Flags filenames.  
-m	 :	Displays the names as a comma-separated list.  
-t	 :	Displays newest files first. (based on timestamp)  
-1	 :	Displays each entry on a line.  

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > **xargs** is a command that helps to build and execute command lines from *standard input*. It is commonly used together with **find** and **grep** where it facilitates the division of a huge list of arguments into a smaller list to allow these smaller argument chunks to be executed.  


> > TO DO ADD example...

> > Helpful Refs:   
- http://javarevisited.blogspot.com/2012/06/10-xargs-command-example-in-linux-unix.html#ixzz4HoWeZhV1  
- https://en.wikipedia.org/wiki/Xargs | http://www.thegeekstuff.com/2013/12/xargs-examples   
- http://www.computerhope.com/unix/xargs.htm  
- http://www.thegeekstuff.com/2013/12/xargs-examples  

