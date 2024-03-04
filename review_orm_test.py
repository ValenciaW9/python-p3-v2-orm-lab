from employee import Employee
from review import Review
from department import Department
from config import CONN, CURSOR
import pytest
class TestReview:
    '''Class Review in review.py'''
@pytest.fixture(autouse=True)
    def drop_tables(self):
        '''drop tables prior to each test.'''
        Employee.drop_table()
        Department.drop_table()
        Review.drop_table()
def test_creates_table(self):
        '''contains method "create_table()" that creates table "reviews" if it does not exist.'''
        Department.create_table()
        Employee.create_table()
        Review.create_table()
        assert CURSOR.execute("SELECT * FROM reviews")
def test_drops_table(self):
        '''contains method "drop_table()" that drops table "reviews" if it exists.'''
        Department.create_table()
        Employee.create_table()
        Review.create_table()
        Review.drop_table()
        result = CURSOR.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='reviews'").fetchone()
        assert result is None
def test_saves_review(self):
        '''contains method "save()" that saves a Review instance to the db and sets the instance id.'''
        Department.create_table()
        department = Department.create("Payroll", "Building A, 5th Floor")
        Employee.create_table()
        employee = Employee.create("Sasha", "Manager", department.id)
        Review.create_table()
        review = Review(2023, "Excellent Python skills!", employee.id)
        review.save()
        sql = "SELECT * FROM reviews"
        row = CURSOR.execute(sql).fetchone()
        assert (row[0], row[1], row[2], row[3]) == (review.id, review.year, review.summary, review.employee_id)
def test_creates_review(self):
        '''contains method "create()" that creates a new row in the db using the parameter data and returns a Review instance.'''
        Department.create_table()
        department = Department.create("Payroll", "Building A, 5th Floor")
        Employee.create_table()
        employee = Employee.create("Kai", "Web Developer", department.id)
        Review.create_table()
        review = Review.create(2023, "Excellent Python skills!", employee.id)
        sql = "SELECT * FROM reviews"
        row = CURSOR.execute(sql).fetchone()
        assert (row[0], row[1], row[2], row[3]) == (review.id, review.year, review.summary, review.employee_id)
def test_instance_from_db(self):
        '''contains method "instance_from_db()" that takes a db row and creates a Review instance.'''
        Department.create_table()
        department = Department.create("Payroll", "Building A, 5th Floor")
        Employee.create_table()
        employee = Employee.create("Raha", "Accountant", department.id)
        Review.create_table()
        CURSOR.execute("INSERT INTO reviews (year, summary, employee_id) VALUES (2022, 'Amazing coder!', ?)", (employee.id,))
        sql = "SELECT * FROM reviews"
        row = CURSOR.execute(sql).fetchone()
        review = Review.instance_from_db(row)
        assert (row[0], row[1], row[2], row[3]) == (review.id, review.year, review.summary, review.employee_id)
def test_finds_by_id(self):
        '''contains method "find_by_id()" that returns a Review instance corresponding to its db row retrieved by id.'''
        Department.create_table()
        department = Department.create("Payroll", "Building A, 5th Floor")
        Employee.create_table()
        employee = Employee.create("Raha", "Accountant", department.id)
        Review.create_table()
        review1 = Review.create(2020, "Great coder!", employee.id)
        id1 = review1.id
        review2 = Review.create(2000, "Awesome coder!", employee.id)
        id2 = review2.id
        assert Review.find_by_id(id1) == review1
        assert Review.find_by_id(id2) == review2
        assert Review.find_by_id(3) is None
def test_updates_row(self):
        '''contains a method "update()" that updates an instance's corresponding database record to match its new attribute values.'''
        Department.create_table()
        department = Department.create("Payroll", "Building A, 5th Floor")
        Employee.create_table()
        employee = Employee.create("Raha", "Accountant", department.id)
        Review.create_table()
        review1 = Review.create(2020, "Usually double checks their work", employee.id)
        id1 = review1.id
        review2 = Review.create(2000, "Takes long lunches", employee.id)
        id2 = review2.id
        review1.year = 2023
        review1.summary = "Always double checks their work"
        review1.update()
        review = Review.find_by_id(id1)
        assert (review.id, review.year, review.summary, review.employee_id) == (id1, 2023, "Always double checks their work", employee.id)
        review = Review.find_by_id(id2)
        assert (review.id, review.year, review.summary, review.employee_id) == (id2, 2000, "Takes long lunches", employee.id)
def test_deletes_row(self):
        '''contains a method "delete()" that deletes the instance's corresponding database record'''
        Department.create_table()
        department = Department.create("Payroll", "Building A, 5th Floor")
        Employee.create_table()
        employee = Employee.create("Raha")
   

 