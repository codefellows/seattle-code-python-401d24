# Django with TailWind + Flowbite

## TailwindCSS

[TailwindCSS](https://tailwindcss.com/){:target="_blank"} is a `utility-first` css framework that represents a fresh (and sometimes controversial) take on styling web sites. Lots of developers find this approach faster and more maintainable than previous approaches. We're all going to try this tool out today.

## Flowbite

[Flowbite](https://flowbite.com/){:target="_blank"} is a very handy tool that builds on top of TailwindCSS and gives access to an excellent set of components. It also includes tools for integrating with popular frameworks, including Django of course!

## Setting up Flowbite with Django

In order to integrate Flowbite with Django it takes a few steps.

**NOTE:** These getting started steps were based on the excellent [Tailwind CSS Django - Flowbite](https://flowbite.com/docs/getting-started/django/){:target="_blank"}, just with some tweaks to work better for our labs. Thanks Flowbite!

### Django Compressor

Install `django-compressor` by running the following command in your terminal:
> `python -m pip install django-compressor`

Add compressor to the installed apps inside the settings.py file:

```python
# config/settings.py

INSTALLED_APPS = [
    ...
    'compressor',
    ...
]
```

1. Configure the compressor inside the settings.py file:

```python
COMPRESS_ROOT = BASE_DIR / 'static'

COMPRESS_ENABLED = True

STATICFILES_FINDERS = ('compressor.finders.CompressorFinder',)
```

1. Create two new folders and an input.css file inside the static/src/ folder:

```text
static
└── src
    └── input.css
```

## Edit base.html

Edit `base.html` file inside the templates/ directory:

```django
<!-- templates/base.html -->

{\% load compress \%}
{\% load static \%}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django + Tailwind CSS + Flowbite</title>

    {\% compress css \%}
    <link rel="stylesheet" href="{\% static 'src/output.css' \%}">
    {\% endcompress \%}

</head>

<body class="bg-green-50">
    <div class="container mx-auto mt-4">
        {\% block content \%}
        {\% endblock content \%}
    </div>
</body>

</html>
```

### Edit home.html

Edit the homepage markup:

```django
<!-- templates/index.html -->

{\% extends "base.html" \%}

{\% block content \%}
  <h1 class="text-3xl text-green-800">Django + Tailwind CSS + Flowbite</h1>
{\% endblock content \%}
{\% endraw \%}
```

### Install Tailwind CSS

Run the following command the install Tailwind CSS as a dev dependency using NPM:
> `npm install -D tailwindcss`
Using the Tailwind CLI create a new tailwind.config.js file:
> `npx tailwindcss init`

Configure the template paths using the content value inside the Tailwind configuration file:

```javascript
module.exports = {
  content: [
      './templates/**/*.html'
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Import the Tailwind CSS directives inside the input.css file:

```css
/* static/src/input.css */

@tailwind base;
@tailwind components;
@tailwind utilities;
```

Run the following command to watch for changes and compile the Tailwind CSS code:
> `npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch`

Open `localhost:3000` in your browser and you’ll see working HTML with Tailwind CSS code.

### Install Flowbite (Stretch)

Now that you have configured both Django and Tailwind CSS you can also set up Flowbite to get access to the whole collection of interactive components like navbars, modals, dropdowns, buttons, and more to make development even faster.

About Flowbite #

Flowbite is an open source library of interactive components built on top of Tailwind CSS and it can be installed using NPM and required as a plugin inside Tailwind CSS.

Install Flowbite as a dependency using NPM:
> `npm install flowbite`

Require Flowbite as a plugin inside the tailwind.config.js file:

```javascript
module.exports = {

    plugins: [
        require('flowbite/plugin')
    ]

}
```

Include Flowbite inside the content value of the tailwind.config.js file:

```javascript
module.exports = {
  content: [
      './templates/**/*.html',
      './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Include Flowbite’s JavaScript file inside the base.html file just before the end of the <body> tag using CDN or by including it directly from the node_modules/ folder:

```javascript
<script src="https://cdnjs.cloudflare.com/ajax/libs/flowbite/1.6.2/flowbite.min.js"></script>
```

Now that you have everything configured you can check out the components from Flowbite such as navbars, modals, buttons, datepickers, and more.

## Flowbite components

In this section I’ll show you how you can search for and use the interactive components from Flowbite.

Let’s start by adding a Navbar component inside the base.html file:

```django
<!-- templates/base.html -->

{\% load compress \%}
{\% load static \%}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django + Tailwind CSS + Flowbite</title>

    {\% compress css \%}
    <link rel="stylesheet" href="{\% static 'src/output.css' \%}">
    {\% endcompress \%}

</head>

<body class="bg-green-50">

    <!-- Add this -->
    <nav class="bg-green-50 border-gray-200 px-2 sm:px-4 py-2.5 rounded dark:bg-gray-800">
        <div class="container flex flex-wrap items-center justify-between mx-auto">
          <a href="{{ .Site.Params.homepage }}/" class="flex items-center">
              <img src="/docs/images/logo.svg" class="h-6 mr-3 sm:h-9" alt="Flowbite Logo" />
              <span class="self-center text-xl font-semibold whitespace-nowrap dark:text-white">Flowbite Django</span>
          </a>
          <button data-collapse-toggle="mobile-menu" type="button" class="inline-flex items-center p-2 ml-3 text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600" aria-controls="mobile-menu" aria-expanded="false">
            <span class="sr-only">Open main menu</span>
            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd"></path></svg>
            <svg class="hidden w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
          </button>
          <div class="hidden w-full md:block md:w-auto" id="mobile-menu">
            <ul class="flex flex-col mt-4 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium">
              <li>
                <a href="#" class="block py-2 pl-3 pr-4 text-white bg-green-700 rounded md:bg-transparent md:text-green-700 md:p-0 dark:text-white" aria-current="page">Home</a>
              </li>
              <li>
                <a href="#" class="block py-2 pl-3 pr-4 text-gray-700 border-b border-gray-100 hover:bg-gray-50 md:hover:bg-transparent md:border-0 md:hover:text-green-700 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">About</a>
              </li>
              <li>
                <a href="#" class="block py-2 pl-3 pr-4 text-gray-700 border-b border-gray-100 hover:bg-gray-50 md:hover:bg-transparent md:border-0 md:hover:text-green-700 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">Services</a>
              </li>
              <li>
                <a href="#" class="block py-2 pl-3 pr-4 text-gray-700 border-b border-gray-100 hover:bg-gray-50 md:hover:bg-transparent md:border-0 md:hover:text-green-700 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">Pricing</a>
              </li>
              <li>
                <a href="#" class="block py-2 pl-3 pr-4 text-gray-700 hover:bg-gray-50 md:hover:bg-transparent md:border-0 md:hover:text-green-700 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent">Contact</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    <!-- End of new HTML -->

    <div class="container mx-auto mt-4">
        {\% block content \%}
        {\% endblock content \%}
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/flowbite/1.6.2/flowbite.min.js"></script>
</body>

</html>
```

This way you already have a functional and responsive navigation bar added to all pages.

Let’s take a look how can added more content directly to the view templates, not just the base template.

Check out one of the Card components from Flowbite and add it to the index.html file:

```django
<!-- templates/index.html -->

{\% extends "base.html" \%}

{\% block content \%}

<h1 class="mb-6 text-3xl text-green-800">Django + Tailwind CSS + Flowbite</h1>
<div class="max-w-sm bg-white border border-gray-200 rounded-lg shadow-md dark:bg-gray-800 dark:border-gray-700">
    <a href="#">
        <img class="rounded-t-lg" src="/docs/images/blog/image-1.jpg" alt="" />
    </a>
    <div class="p-5">
        <a href="#">
            <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Noteworthy technology
                acquisitions 2021</h5>
        </a>
        <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">Here are the biggest enterprise technology
            acquisitions of 2021 so far, in reverse chronological order.</p>
        <a href="#"
            class="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-green-700 rounded-lg hover:bg-green-800 focus:ring-4 focus:outline-none focus:ring-green-300 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800">
            Read more
            <svg class="w-4 h-4 ml-2 -mr-1" fill="currentColor" viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd"
                    d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                    clip-rule="evenodd"></path>
            </svg>
        </a>
    </div>
</div>

{\% endblock content \%}
```

## Improving Home Page

Grab the [Flowbite Card with Image](https://flowbite.com/docs/components/card/#card-with-image) and use it to render out a `card` for each `thing` in data. This will require adjustments from the Flowbite's sample code. See `home.html` in demo for final version.

## Improving About Page

Follow the same process for About page using [Flowbite User profile card](https://flowbite.com/docs/components/card/#user-profile-card). This will require adjustments from the Flowbite's sample code. See `about.html` in demo for final version.

## Wrapping Up

At this point you can use any of the components to build user interfaces easier and faster together with Django, Tailwind CSS and Flowbite.
