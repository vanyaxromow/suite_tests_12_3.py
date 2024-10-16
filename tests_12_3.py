import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        some_obj_1 = Runner('Mark')
        for i in range(10):
            some_obj_1.walk()
        self.assertEqual(some_obj_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        some_obj_2 = Runner('Tom')
        for i in range(10):
            some_obj_2.run()
        self.assertEqual(some_obj_2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        some_obj_3 = Runner('Nil')
        some_obj_4 = Runner('Nail')
        for i in range(10):
            some_obj_3.run()
            some_obj_4.walk()
        self.assertNotEqual(some_obj_3.distance, some_obj_4.distance)


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.usain = Runner('Usain', 10)
        self.andrey = Runner('Andrey', 9)
        self.nick = Runner('Nick', 3)

    @classmethod
    def tearDownClass(cls):
        for i in TournamentTest.all_results:
            print(i)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_1(self):
        obj_1 = Tournament(90, self.usain, self.nick)
        TournamentTest.all_results.append(obj_1.start())
        self.assertTrue(self.all_results[0][2] == self.nick.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_2(self):
        obj_2 = Tournament(90, self.andrey, self.nick)
        TournamentTest.all_results.append(obj_2.start())
        self.assertTrue(self.all_results[1][2] == self.nick.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_3(self):
        obj_3 = Tournament(90, self.andrey, self.usain, self.nick)
        TournamentTest.all_results.append(obj_3.start())
        self.assertTrue(self.all_results[2][3] == self.nick.name)