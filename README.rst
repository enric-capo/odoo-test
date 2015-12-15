Lot Get Name Quantity
#####################

This module displays available quantity associated with a Lot. According to Odoo
help for this field, **Available Quantity** is:

    | **Current quantity of products.** 
    | In a context with a single Stock Location, this includes goods stored at this Location, or any of its children. 
    | In a context with a single Warehouse, this includes goods stored in the Stock Location of this Warehouse, or any of its children, stored in the Stock Location of the Warehouse of this Shop, or any of its children. 
    | Otherwise, this includes goods stored in any Stock Location with 'internal' type.


Technical Info
**************

It extends ``stock.production.lot.name_search()`` method, adding
``qty_available`` value calculated from
``product.product._product_available()``.


Credits
*******

Maintainer
==========

.. image:: http://www.minorisa.net/wp-content/themes/minorisa/img/logo-minorisa.png
    :alt: Minorisa.net
    :target: http://www.minorisa.net


Contributors
============

* Jaume Planas <jaume.planas@minorisa.net>

 