# Technology Stack

The Frontend will be build based on 3 Languages/Frameworks: 

* HTML for the Layout
* Bootstrap for a modern styling of the html 
* Typescript for the reactivity

# HTML 

## Basics 

* Basic Layout of an empty HTML File

```HTML
 <!DOCTYPE html> #HTML 5 Declaration
<html>
<head></head> # Loading Scripts 
<body> # Actual content displayed

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html> 
```

* __Elements__: <tagname>Content</tagname> -> <h1>Große Schrift</h1> 
* __Attributes__: Elements can have attributes <a> -> Hyperling <a href=www.max.de>Visit my site</a>
More attributes, e.g. img tag:
    * src: Source of an image
    * alt: Alternative text for image
    * lang: <html lang="en">
--> Always use qoutes for attribute values

## Style Attribute

* Add style to a tag, e.g. <body style="background-color: powderblue;">...</body>

    * Use the __style__ attribute for styling HTML elements
    * Use __background-color__ for background color
    * Use __color__ for text colors
    * Use __font-family__ for text fonts
    * Use __font-size__ for text sizes
    * Use __text-align__ for text alignment

### Stylesheets einbinden

* Externe Sheets 

```HTML
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
```
* Externe Scripts werden mit <script> tag eingebunden.
## Class Attribute

* Usually used to refer to a css class (e.g. .city {background-color: tomato; color: white ; ....} -> city is class) 

## Div and span

* Useful with css to apply a styling to a block of 
* Div is a block-element -> Uses the entire screen (If not specified different in css)
* Span is an inline element and can be used to style text inline -> Examples

```HTML
<div style="background-color:red;">
  Steuerung
</div>
ein <span style="background-color:yellow;">wie vom Textmarker 
hervorgehobener</span> Text und dann geht es normal weiter
```

# Bootstrap

## Basics

* Must be included in head <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
* 