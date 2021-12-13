import pytest
import os
from class_score import Score


@pytest.fixture
def score_test():
   return Score('Joueur', 50)

class TestScore():
    def test_init(self, score_test):
        assert score_test.name == 'Joueur'
        assert type(score_test.name) == str
        assert score_test.score == 50
        assert type(score_test.score) == int
        
   #  def test_save_score(self,tmpdir, score_test):
   #      p = tmpdir.mkdir("tempdir")
   #      score_test.save_score(path=p)
   #      assert os.path.exists(os.path.join(p,f'scores.csv')) == True