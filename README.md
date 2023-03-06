# TestBotToBootcamp
link :https://t.me/TestToBootcamp_bot

## Инструкция по запуску через докер

* Используя https://t.me/BotFather создайте бота в телеграм
* Скопируйте полученный токен в ENV TOKEN в dockerfile
* В терминале создайте образ при помощи команды ```build .```
* Используя команду ```docker images``` получем id образа
* Далее, используем команду ```docker run -d -p 80:80 <id_image>```, подставляя полученный на прошлом шаге id, запускаем бота
* Для остановки бота воспользуйтесь командой ```docker stop <id_container>```. id контейнера можно получить воспользовавшись командой ```docker stop```

