from mrjob.job import MRJob

class salarySE(MRJob):

  def mapper(self, _, line):
    idemp, sececon, salary, year = line.split(',')
    try:
      salary = float(salary)
    except ValueError:
      pass
    else:
      yield sececon, salary
      
  def reducer (self, sececon, salaries):
    sum_salaries = 0
    cont = 0
    for sal in salaries:
      sum_salaries = sum_salaries + sal
      cont = cont +1
        
    yield sececon, sum_salaries / cont

if __name__ == '__main__':
  salarySE.run()
        
    