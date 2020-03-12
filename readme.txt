This is you repo root folder which contains .git folder
Do not delete this folder. 
***********************************************************************************************************************
Add all your project files into this folder and follow below steps
git add .
git commit -a -m" inital commit"
git push
***********************************************************************************************************************
NOTE:
If Folder is empty you cannot commit.
By default all repo will come with master branch.
***********************************************************************************************************************
To create a new branch 
git branch <branch name> ( This will create a branch from current branch)
git push -u origin <branch name>
***********************************************************************************************************************
To push your code, follow below steps
git add .
git commit -a -m" inital commit"
git push
***********************************************************************************************************************
To switch your branch 
git checkout <branch name>
***********************************************************************************************************************
Eg: To copy you old project files
	DjangoTest ( Lets say this is your Old project folder)

	CustomAdmin ( New project folder, which I have sent)

copy all files and folder from DjangoTest folder and paste it into  CustomAdmin folder  then just run below commands
git add .
git commit -a -m" inital commit"
git push
	
