# TEDxTehran - Event Application Backend

![](https://upload.wikimedia.org/wikipedia/commons/b/b9/TEDxTehran.png)

![](https://img.shields.io/github/stars/TEDxTehran-Team/event-app-core) ![](https://img.shields.io/github/forks/TEDxTehran-Team/event-app-core) ![](https://img.shields.io/github/issues/TEDxTehran-Team/event-app-core)

## About
> Supporting the mission of Ideas Worth spreading, TEDxTehran are local, independently organized events licensed by TED that brings people living in Tehran together to share a TED-like experience. We bring thought leaders, innovators and doers, from across different disciplines, to share their ideas and stories in the heart of Tehran. In the spirit of TED’s “Ideas Worth Spreading” we strive to bring "Make Iran Famous for its Ideas".

This is the repository hosting the code for **the backend of TEDxTehran's event application**, free for use by anyone.

## Requirements
- Docker (version 19.03.0 or later)
- Docker compose

## Deploy
- Clone the repo:
`git clone git@github.com:TEDxTehran-Team/event-app-ios.git`
- Copy .env.example to .env
- Copy .env.local.example - or .env.production.example depending on where you are deploying - to .env.local
- Add secret key and other data to the env files
- Run these commands:
```shell
docker-compose up
docker-compose exec app python manage.py migrate
```

## Demo
You can visit the demo deployment of this project [here](http://demo-backend.tedxtehran.com:8000/)

To access the admin panel use the following credentials:
* Username: admin
* Password: admin

For now we have left the `debug=True` for ease of debug and usage.

## Contributing
Feel free to submit any pull request that improves this project in any possible way. Before undertaking a major change, consider opening an issue for some discussion.

## Roadmap
Here are the list of features we intend to include in this project. The ones that are checked have been finished.

- [x] Event Management (including talks, speakers, timeline, gallary and sponsors)
- [x] Preparing the project for running on Docker
- [ ] Model Structure in UML
- [ ] User Profile and Login
- [ ] In-app Networking ( Chat )
- [ ] Eventday Check-in


## Other Open-Source Projects
- [iOS application](https://github.com/TEDxTehran-Team/event-app-ios)
- [Android application](https://github.com/TEDxTehran-Team/event-app-andoid)
