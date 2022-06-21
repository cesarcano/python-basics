-----------------------------------------------------------
    GUIA BASICA DE COMANDOS GIT	
-----------------------------------------------------------
------------------------------------------------------------

----------------------
--- Inicio básico ----
----------------------

# Iniciar  un proyecto
    git init

# Clonar un proyecto
    git clone [repo url]

# Verificar status un repositorio -> Muestra el estatus del repositorio (rama, archivos con cambios, etc)
    git status
	
# Verificar archivos en 'stage'
	git diff --name-only --cached

---------------
--- Branch ----
---------------

# Listar todas las ramas (remotas y locales)
    git branch -a

# Listar ramas locales 
    git branch -r

# Subir una rama local
    git push -u origin [branch]

# Crear rama local
    git branch [nombre-branch]
	
# Crear rama local a partir de un commit
	# Listar commits para obtener el id de commit -> "git log"
	git branch [branch-name] [commit_id]

# Crear rama local + checkout
    git checkout -b [branch-name]

# Cambiar a rama local
    git checkout [branch-name]

# Cambiar a rama remota
    git checkout --track origin/[branch-name]

# Eliminar branch local
    git branch -d [branch-name]

# Eliminar Branch remota
    git push origin --delete [branch-name]

# Listar commits en un branch (presionar 'q' para salir)
    git log
    git log --pretty=format:"%h | %ae - %ar --> %s"

# Subir rama local
    git push -u origin [branch-name]

# Cambiar nombre de rama actualizada
	git branch -m [nuevo nombre de rama]

-----------------
--- Git TAGs ----
-----------------

# Refrescar tags 
	git fetch --all --tags

# listar tags
	git tag -l

# checkout en un tag
	git checkout tags/[tag_name] -b [branch-name]
	
# Eliminar un tag local
	git tag -d [tag_name]
	
# Eliminar un Tag remoto
	git push --delete origin [tag-name]
	
# Crear un tag (se debe hacer después de un commit)
	git tag [tag_name] -m "[Mi mensaje]"

# Subir un tag
	git push origin [tag-name]
	
# Crear o modificar un tag
	
	1) Create a branch with the tag
		git branch [branch-name] [tagname]
		git checkout [branch-name]

	2) Include the fix manually if it's just a change .... 
		git add .
		git commit -m '[Commit's Message]'
		
	3) Delete and recreate the tag locally
		git tag -d [tag_name]
		git tag [tagname]

	4) Delete and recreate the tag remotely
		git push origin :[tagname] // deletes original remote tag
		git push origin [tagname] // creates new remote tag
			
	5)  Update local repository with the updated tag 
		git fetch --tags

----------------------------------------------
--- Stash (guardado de cambios sin commit) ---
----------------------------------------------

# Stash básico (respalda todos los archivos con cambios)
    git stash

# Stash con mensaje (parecido a un commit)
    git stash save '[Mensaje o nombre de etiqueta]'

# Stash parciales (se van a iterar los archivos con cambios)
    git stash -p

Comandos para ejecutar acción dado un archivo                                 
|-------------------------------------------------------------------------------|
| Comando |	Descripción                                                         |
|-------------------------------------------------------------------------------|
|   /     |	buscar un hunk mediante expresiones regulares                       |
|   ?     |	Ayuda                                                               |
|   n     |	no guardar este hunk en un stash                                    |
|   q     |	salir (se guardarán en un stash todos los hunks ya seleccionados)   |
|   s     |	dividir este hunk en otros más pequeños                             |
|   y     |	guardar este hunk en un stash                                       |
---------------------------------------------------------------------------------    

# Aplicar cambios quitando stash (stash sencillo)
    git stash pop

# Ver lista de stash
    git stash list

# Crear rama a partir de stash
    git stash branch [branch-name] stash@{[index ej. 0]}

# Aplicar stash y eliminarlo de la lista de stash
    git stash pop stash@{[index ej. 0]}
    
# Aplicar stash sin eliminar de la lista de stash
    git stash apply stash@{[index ej. 0]}

# limpiar lista de stash
    git stash clear 

# Eliminar un stash
    git stash drop stash@{1}

-----------------------
--- Hacer un commit ---
-----------------------

# Agregando un archivo
    git add [nombre_de_archivo.something]

# Agregando todos los archivos
    git add .
    git add --all

# Hacer un commit
    git commit -m '[commit message]'

# Subir cambios
    git push

# Bajar cambios
    git pull
	
# Agregar cambios a ultimo commit
	
	# Agregar a stage
		git add [. or files]
	
	# Agregando cambios a último commit
		git commit --amend --no-edit
	
# Modificar mensaje de ultimo commit
	git commit --amend -m "an updated commit message"

-------------
--- Merge ---
-------------

Suponiendo que existe una rama de nombre develop y se crea la rama new-feature para trabajar en nuevas funcionalidades;
es de esperarse que posteriormente se requiera integrar a develop estos nuevos cambios y que exista más de una persona 
actualizando esta rama constantemente; antes de hacer merge, se debe asegurar que la rama develop esté actualizada y 
luego, que la rama new-feature sea actualizada con los últimos cambios de develop, por lo que, para este caso se seguirán 
los siguientes pasos:

1. Aplicar un stash para respaldar los cambios existentes en new-feature (si aplica):

    git stash save 'AAMMDDHHmm-Nuevos-cambios'

2. Hacer checkout a develop y actualizar:

    # Cambiando a rama develop...
    git checkout develop

    # Actualizando rama local...
    git pull

3. Actualizar new-feature con lo último de develop:

    # Cambiando a rama new-feature
    git checkout new-feature

    # Actualizando new-feature con contenido de develop
    git merge develop

4. Aplicar los cambios que se respaldaron en el punto 1.

    # Se listan los stash
    git stash list

    # Se recupera stash, 
    # para este ejemplo el stash se encuentra en el indice 0 de la lista
    git stash pop stash@{0}

    # Se preparan archivos para commit
    git add .

    # Se hace commit con los nuevos cambios
    git commit -m 'Nuevos cambios'

5. Actualizar develop con el contenido de new-feature:

    # Cambiando a develop para actualizar desde new-feature 
    git checkout develop

    # Merge new-feature -> develop
    git merge new-feature

    # Actualizando origin/develop
    git push

Nota: Para este ejemplo, es recomendable actualizar new-feature cada que origin/develop reciba un push.

---------------------------------------
--- Hacer migración de repositorios ---
---------------------------------------

1. Hacer un mirror del repositorio a migrar
	# Se descarga el repositorio en una carpeta temporal, el repo no incluye ORIGIN
	git clone --mirror [PATH ORIGEN ACTUAL] temp-repo

2. Remover origin
	git remote rm origin
	
3. Agregar nuevo origin
	git remote add origin [NUEVO PATH ORIGEN]

3. Actualizar nuevo origin 
	git push origin --all
