"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
brand_id_8 = Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
model_chev_corvette = Model.query.filter(Model.name=='Corvette', Model.brand_name=='Chevrolet').all()

# Get all models that are older than 1960.
predates_1960 = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
brands_post_1920 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
cor_names = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
est_1903 = Brand.query.filter(Brand.founded==1903, Brand.discontinued.is_(None))

# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.
disc_or_predates_1950 = Brand.query.filter(db.or_(Brand.discontinued.isnot(None)), (Brand.founded < 1950))

# Get any model whose brand_name is not Chevrolet.

not_chevrolet = Model.query.filter(Model.brand_name != 'Chevrolet').first()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = Model.query.filter(Model.year == year).all()

    #Used formatting syntax learned from http://www.openbookproject.net/thinkcs/python/english2e/ch07.html

    print "%-10s \t %-10s \t %-10s" % (
        "MODEL NAME", "BRAND NAME", "HEADQUARTERS")

    for model in models:
        print ""
        print ("%-10s \%-10s \%-10s" % 
              (model.name, model.brand_name, model.brand.headquarters))





def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    

    brands = Brand.query.all()

    result = ""

    for brand in brands:
        result += "\n" + brand.name + ":\n"
        #brand and models table linked via line 29 in model.py
        for model in brand.models:
            result += "\t%s\n" % model.name

    print result


# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
    # Brand.query.filter_by(name='Ford') returns:
    #<flask_sqlalchemy.BaseQuery object at 0x1030b7710>. This is a query object
    #and points to a space in the computer's memory. No record is fetched until .all(), .first(), .one()
    #are added.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
    #An association table provides a link between tables that have a many to many relationship. 
    #It contains no meaningful information of it's own but typically uses foreign keys of the two tables 
    #one wishes to link to associate them.

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    """Takes in any string as parameter, and returns a list of objects 
    that are brands whose name contains or is equal to the input string"""
    brands = Brand.query.filter(Brand.name.like("%" + mystr + "%")).all()

    return brands


def get_models_between(start_year, end_year):
    """Takes a start year and end year (two integers), and returns a list of objects that 
    are models with years that fall between the start year (inclusive) and 
    end year (exclusive)."""
    models = Model.query.filter(Model.year >= start_year, Model.year < end_year)
    
    return models







