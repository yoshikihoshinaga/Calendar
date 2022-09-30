#
#Author:Yoshiki Hoshinaga
#Date: June 16
# ps11pr2.py (Problem Set 11, Problem 2)
#
# A class to represent calendar dates
#

class Date:
    """ A class that stores and manipulates dates,
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, new_month, new_day, new_year):
        """ The constructor for objects of type Date. """
        self.month = new_month
        self.day = new_day
        self.year = new_year

    # The function for the Date class that returns a Date
    # object in a string representation.
    
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this _can_ be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year. Otherwise, returns False.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        """ Returns a new object with the same month, day, year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date
    
    def advance_one(self):
        """ changes the called object so that it represents 
            one calendar day after the date that it originally 
            represented.
        """
        fdays = 28 + self.is_leap_year()
        days_in_month  = [0,31,fdays,31,30,31,30,31,31,30,31,30,31]
        self.day += 1
        if self.day > days_in_month[self.month]:
            self.day = 1
            self.month += 1
            if self.month == 13:
                self.year += 1
                self.month = 1
        return self.day
    
    def advance_n(self,n):
        """changes the calling object so that it represents n
            calendar days after the date it originally represented.
            Additionally, the method should print all of the dates 
            from the starting date to the finishing date, inclusive 
            of both endpoints.
        """
        for i in range(0, n):
            print (self)
            self.advance_one()
        print (self)

    def __eq__(self,other):
        """returns True if the called object (self) and the argument (other) 
            represent the same calendar date (i.e., if the have the same values for their day, 
            month, and year attributes). Otherwise, this method should return False.
        """
        if self.day==other.day and self.month==other.month and self.year==other.year:
            return True 
        else:
            return False

    def is_before (self, other):
        """returns True if the called object represents a calendar date 
            that occurs before the calendar date that is represented by other.
            If self and other represent the same day, or if self occurs after other, 
            the method should return False.
        """
        if other.year != self.year:
            return self.year < other.year
        if other.month != self.month:
            return self.month < other.month
        return self.day < other.day

    def is_after (self, other):
        """ returns True if the calling object represents a calendar date 
            that occurs after the calendar date that is represented by other. 
            If self and other represent the same day, or if self occurs before other,
            the method should return False.
        """
        if other.year != self.year:
            return self.year > other.year
        if other.month != self.month:
            return self.month > other.month
        return self.day > other.day
    
    def days_between(self, other):
        """returns an integer that represents the number of days between self and other.
        """
        d1 = self.copy()
        d2 = other.copy()
        between = 0
        if self.__eq__(other) == True:
            return 0
        else:
            if self.is_before(other) == True:
                while (d1.__eq__(other) != True):
                    between = between + 1
                    d1.advance_one()
            elif self.is_after(other) == True:
                while (d2.__eq__(self) != True):
                    between = between + 1
                    d2.advance_one()
        if self.is_before(other) == True:
            return between * -1
        else:
            return between
   
    def day_name(self):
        """returns a string that indicates the name of the day 
        of the week of the Date object that calls it. In other words, 
        the method should return one of the following strings: 
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'.
        """
        days =[ "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        temp = [ 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 ]
        yr = self.year
        if self.month < 3 :
            yr -= 1
        dayOfname = (( yr + int(yr / 4) - int(yr / 100)+ int(yr / 400) + temp[self.month - 1] + self.day) % 7)
        return days[int(dayOfname)]

#### Put your code for problem 2 below. ####
if __name__ == '__main__':
#test 1
    d1 = Date(4, 15, 2019)
    print('d1.mouth',d1.month)
    print('d1.day',d1.day)
    print('d1.year',d1.year)
    print('')
#test 2
    d1 = Date(4, 8, 2019)
    print('d1',d1)
    print('Leap Year : ' + str(d1.is_leap_year()))
    d2 = Date(1, 1, 2020)
    print('d2',d2)
    print('Leap Year : ' + str(d2.is_leap_year()))
    print('')
#test 3
    d = Date(12, 31, 2018)
    day = d.__init__(12, 31, 2018)
    d.advance_one()
    print(d)
    d = Date(2, 28, 2020)
    day = d.__init__(2, 28,2020)
    d.advance_one()
    print(d)
    d.advance_one()
    print(d)
    d.advance_one()
    print(d)
    print('')
#test 4
    d = Date(4, 8, 2019)
    day = d.__init__(4, 8, 2019)
    d.advance_n(3)
    d = Date(4, 8, 2019)
    d.advance_n(0)
    print(d)
    print('')
#test 5
    d1=Date(1, 1, 2020)
    d2=d1
    d3=d1.copy()
    print(d1==d2)
    print(d1==d3)
    print('')
#test 6
    ny = Date(1, 1, 2019)
    d1 = Date(11, 15, 2018)
    d2 = Date(3, 24, 2018)
    tg = Date(11, 22, 2018)
    print(ny.is_before(d1))
    print(d1.is_before(ny))
    print(d1.is_before(d2))
    print(d2.is_before(d1))
    print(d1.is_before(tg))
    print(tg.is_before(d1))
    print(tg.is_before(tg))
    print('')
#test 7
    ny = Date(1, 1, 2019)
    d1 = Date(11, 15, 2018)
    d2 = Date(3, 24, 2018)
    tg = Date(11, 22, 2018)
    print(ny.is_after(d1))
    print(d1.is_after(ny))
    print(d1.is_after(d2))
    print(d2.is_after(d1))
    print(d1.is_after(tg))
    print(tg.is_after(d1))
    print(tg.is_after(tg))
    print('')
#test 8
    d1 = Date(4, 8, 2019)
    d2 = Date(5, 7, 2019)
    print(d2.days_between(d1))
    print(d1.days_between(d2))
    print(d1)
    print(d2)
    d3 = Date(12, 1, 2019)
    d4 = Date(3, 15, 2020)
    print(d4.days_between(d3))
    print('')
#test 9
    d = Date(4, 8, 2019)
    print('d.day_name',d.day_name())
    d = Date(4, 9, 2019).day_name()
    print('d.day_name',d)
    d = Date(4, 10, 2019).day_name()
    print('d.day_name',d)
    d = Date(1, 1, 2100).day_name()
    print('d.day_name',d)
    d = Date(7, 4, 1776).day_name()
    print('d.day_name',d)



def nye_counts(start, end):

    d = {} # create an empty dictionary
    d['Sunday'] = 0
    d['Monday'] = 0
    d['Tuesday'] = 0
    d['Wednesday'] = 0
    d['Thursday'] = 0
    d['Friday'] = 0
    d['Saturday'] = 0
    # add your code here
    for year in range (start, end+1):
        date = Date (12, 31, year)
        day = date.day_name()
        if day in d.keys():
            d[day] = d[day]+1 
        else:
            d[day] = 1
    return d

if __name__=='__main__':
    counts = nye_counts(2014, 2113)
    print(counts)
    print(counts['Wednesday'])
    counts = nye_counts(2018, 2019)
    print(counts)
