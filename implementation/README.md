The implementation of an MVP for Shorten consists of three files

* UX (provided by the user-agent, i.e. a browser)
* buisness logic
  + `.htaccess` -- Apache rewriting of the URL
  + `s.cgi` -- Bash script to send browser a 302 with the new Location (Permissions: 755)
* database
  + `s` -- tab-delimited flat file (logically a table with two columns)

```
├── public_html
│   ├── .htaccess
│   └── cgi-bin
│       └── s.cgi
└── shortcuts
    └── s
```
