#2.4. Инструменты Git

1. Найдите полный хеш и комментарий коммита, хеш которого начинается на aefea.

git show aefea


2. Какому тегу соответствует коммит 85024d3?
  
v0.12.23

3. Сколько родителей у коммита b8d720? Напишите их хеши.

56cd7859e0, 9ea88f22fc
  
4. Перечислите хеши и комментарии всех коммитов которые были сделаны между тегами v0.12.23 и v0.12.24.

[Website] vmc provider links b14b74c4
Update CHANGELOG.md 3f235065
registry: Fix panic when server is unreachable 6ae64e24
website: Remove links to the getting started guide's old location 5c619ca1
Update CHANGELOG.md 06275647
command: Fix bug when using terraform login on Windows d5f9411f
Update CHANGELOG.md 4b6d06cc
Update CHANGELOG.md dd01a350
Cleanup after v0.12.23 release 225466bc
  
5. Найдите коммит в котором была создана функция func providerSource, ее определение в коде выглядит так func providerSource(...) (вместо троеточего перечислены аргументы).

5af1e623
  
6. Найдите все коммиты в которых была изменена функция globalPluginDirs.

8364383c, 78b12205, 41ab0aef, 52dbf948
  
7. Кто автор функции synchronizedWriters?

Martin Atkins
