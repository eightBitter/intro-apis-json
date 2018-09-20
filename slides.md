# Introduction to APIs and JSON

---

## Outline

- Intro to APIs
- Intro to JSON
- Exercise: Explore an API

---

# Intro to APIs

---

## What is an API?

---

## Web APIs

---

## Examples of Web APIs

- [Twitter APIs](https://developer.twitter.com/en/docs.html)
- [Data.gov APIs](https://api.data.gov/)
- [The Star Wars API (SWAPI)](https://swapi.co/)

---

# Intro to JSON

---

## JSON Basics

- JavaScript Object Notation is a data format
- Based on a subset of the JavaScript Programming Language
- Text based and language independent


---

## Simple JSON Example

![alt text](./assets/csv.png)
![alt text](./assets/json.png)

---

## JSON Data Types

- Strings: <span style="color:red">`"name"`</span>`:` <span style="color:green">`"Jacob"`</span>
- Numbers: <span style="color:red">`"age"`</span>`:` <span style="color:orange">`30`</span>
- Objects: <span style="color:red">`"employee"`</span>`:` `{` <span style="color:red">`"name"`</span>`:`<span style="color:green">`"Jacob", "age":30 `</span>`}`
- Arrays: <span style="color:red">`"employees"`</span>`: [`<span style="color:green">`"Jacob", "Walt"`</span>`]`
- Booleans: <span style="color:red">`"librarian"`</span>`:` <span style="color:blue">`true`</span>

[More on JSON Data Types](https://www.w3schools.com/js/js_json_datatypes.asp)

---

## Complex JSON Example

```json
{
  "paintings": [
    {
      "name": "The Scream",
      "url": "https://en.wikipedia.org/wiki/The_Scream",
      "creator": {
        "@type": "Person",
        "name": "Edvard Munch",
        "sameAs": "https://en.wikipedia.org/wiki/Edvard_Munch"
      }
    },
    {
      "name": "Melancholy",
      "url": "https://en.wikipedia.org/wiki/Melancholy_(Edvard_Munch)",
      "creator": {
        "@type": "Person",
        "name": "Edvard Munch",
        "sameAs": "https://en.wikipedia.org/wiki/Edvard_Munch"
      }
    }
  ]
}
```

---

## API/JSON Help(ers)!

- [JSONLint](https://jsonlint.com/)
- [Twitter API Libraries](https://developer.twitter.com/en/docs/developer-utilities/twitter-libraries.html)
  - [TwitteR](https://www.rdocumentation.org/packages/twitteR/versions/1.1.9)
- [Using Data.gov APIs in R](https://data.library.virginia.edu/using-data-gov-apis-in-r/)
- [SWAPI Helper libraries](https://swapi.co/documentation#python)
- [[Microsoft Excel] Connect to a JSON File](https://support.office.com/en-us/article/connect-to-a-json-file-f65207ab-d957-4bf0-bec3-a08bb53cd4c0)

---

# Exercise!

---

## Exercise: Explore SWAPI

Using your weapon of choice (web browser, Python, R, etc), explore SWAPI and answer these questions:

1. Which movies did George Lucas produce?
2. When was The Force Awakens released?
3. According to the API, which planets were featured in The Empire Strikes Back?
  - Which of these planets has the highest pop?

---

## Questions?

**Thank you!**

Jacob Shelby - jtshelby@ncsu.edu

Walt Gurley - jwgurley@ncsu.edu
