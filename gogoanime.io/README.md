# B Corps - API
## AN API TO GET B CORPS BASIC DATA USING FLASK
[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](https://github.com/PRANAVBHATIA1999/B-Corps-API)

## What is B Corps API?
B corps API is for any application which needs  data like company name, industry and the location of a B corp certified company across the globe.

## URL 

```
GET: https://bcorps.herokuapp.com/bcorps
```

## Usage
Just do a GET request on the API URL.
```
GET: https://bcorps.herokuapp.com/bcorps?country=<Country Name>
```

## Arguments
```
<country name>

Name or their codes in ISO 3166-1 alpha-2
```
## Return Format
```
JSON
```
## Example
```
GET: https://bcorps.herokuapp.com/bcorps?country=India
# This will return all B Corps companies listed in India in JSON format.
```

```
GET: https://bcorps.herokuapp.com/bcorps
# This will return the basic data of B Corps comapnies across the globe.
```

```
GET: https://bcorps.herokuapp.com/bcorps?country=US
# This will return the basic data of B corps companies in the United States.
```

## Enhancements
Please feel free to message me or open an issue if you have an idea for an enhancement. Seems like people are starting to use this and I would like to improve it further.

## License
MIT

## Contact 

<p align='center'>
<a href="https://twitter.com/pranavvbhatia">
  <img src="https://img.shields.io/badge/twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" />
</a>&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/bhatiapranav/">
  <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />
</a>&nbsp;&nbsp;
<a href="mailto:pranavbhtaia431999@gmail.com">
  <img src="https://img.shields.io/badge/email me-%23D14836.svg?&style=for-the-badge&logo=gmail&logoColor=white" />
</a>
</p>

## Author 
Pranav Bhatia"# gogoanime.io-flask" 
