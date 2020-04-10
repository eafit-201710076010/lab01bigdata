from mrjob.job import MRJob

class sumSE(MRJob):

  def mapper(self, _, line):
    idemp, sececon, salary, year = line.split(',')


    yield (idemp, (sececon, 1))
      
  def reducer (self, idemp, sececon):
    sum_sec=0
  
    for se, cont in sececon:
      sum_sec = sum_sec + cont
        
    yield idemp, sum_sec

if __name__ == '__main__':
  sumSE.run()