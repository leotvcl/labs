# labs
examples, first steps and other things

Pasos iniciales
git config --global user.name "Pon tu nombre"
git config --global.user.email "Pon tu correo"

Si deseo desde mi computador iniciar un repo:
git init

Si deseo clonar uno existente
git clone https://direccion_del_repo

Para ver el estado de mis cambios
git status
versión resumen
git status -s
para agregar un archivo
git add nombre_del_archivo

Para ver qué he preparado y qué no
git diff

El siguiente comando me permite ver lo que está confirmado
git diff --staged

Eliminar archivos git rm nombre_del_archivo

Cambiar el nombre del archivo
git mv nombre_del_archivo nuevo_nombre_del_archivo

Ver historial de archivos
git log

Deshacer un commit

git commit --amend

ejemplo:
  git commit -m 'Initial Commit'
  git add olvide_este_file.txt
  git commit --amend

Puedo traer otros repos y combinarlos

git remote add pb https://el_repo_remoto
git fetch pb

Enviar los remotos
git push origin master (o main)

Inspeccionar un remoto
git remote show origin

#  Ramas
Crear una Rama
git branch _nombre_de_la_rama

cambiar la Rama
git checkout _nombre_de_la_rama
