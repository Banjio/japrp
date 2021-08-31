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

# Javascript References

## Basic Syntax

* Defining variables:
  * __Keywords__: `var, let, const`
  * var is function scoped (only available in the scrope of a function) while let is block scoped  (scoped in enclosing brackeds {}). Const is immutable
  * All use the same creation syntax ```var/let/const x = 5;```. Or when not assigning a value only creating the variable for later usage
* __Functions__: 
  * ```
    function myFunction(p1, p2) {
      return p1 * p2;   // The function returns the product of p1 and p2
    }
    ```
  * Invokation example: ```let x = myFunction(4,3);```

# Jquery

## Basic Syntax 

![](/home/maxbeier/ws/japrp/web_frontend/readme_pictures/jq_syntax.png)
* Actions for the same selector can be chained, e.g. selector.hide().show()
* Selector.text() &Rightarrow; Get text of selected elements
* Selector.val() &Rightarrow; Get value of forms
* Selector.html() &Rightarrow; Content of selected elements

## Effects 
* .hide(speed,callback);) / .show(speed,callback);) / .toggle(speed,callback) &Rightarrow; Shor or hide HTML Elements or toggle between hiding and showing
  * __Speed__ for showing or hiding "slow", "fast", or milliseconds.
  * __Callback__: Function hat is executed after showing hiding
* __Fading__: Can be used to fadeIn() or fadeOut() Objects (EntireDivs can be faded in) -> Maybe this is a better way than the dropdown Menu as we can fadein entire divs
* 
# NPM 

* Software manager, similiar to pip 

# Radioplayer

## Searchbar 

* For searching the information we use Radio-Browser.infos implemented nodejs module: https://www.npmjs.com/package/radio-browser