# Iugu

The Iugu provides a Python REST APIs to create, process and manage payments.

## Installation

Using pip:

    $ pip install iugu

From source code:

    Clone the source:

        $ git clone git@github.com:iugu/iugu-python.git

    Execute the setup script:

        $ cd iugu-python
        $ python setup.py install

## Usage

You should import and create an iugu instance using your [api token](https://dev.iugu.com/reference#section-criando-suas-chaves-de-api-api-tokens):

```py
import iugu
api = iugu.config(token=IUGU_API_TOKEN)
```

After that you can use the instance to iniciate the module you need, example:

```py
# token api
iugu_token_api = iugu.Token()
# customer api
iugu_customer_api = iugu.Customer()
```

To see all available modules, check the [iugu folder](https://github.com/iugu/iugu-python/tree/master/iugu) of this project.

## Documentation

Visit [iugu.com/referencias/api](http://iugu.com/referencias/api) for api reference or [iugu.com/documentacao](http://iugu.com/documentacao) for full documentation

## Author

Originally by [Felipe Tomaz](https://github.com/lspecian) and [Arthur Furlan](https://github.com/arthurfurlan).

## Contributor

[André Kiffer](https://github.com/andrekiffer).
[Rodolpho Pivetta Sabino](https://github.com/rodolphopivetta).
[Joabe Mendes](https://github.com/JoabMendes).
