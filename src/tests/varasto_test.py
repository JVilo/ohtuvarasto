import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varasto_tyhja(self):
        self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_varasto_taynna(self):
        self.varasto.lisaa_varastoon(10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_ala_ota_mitaan(self):
        self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_otetaan_isompi_maara_kun_varaston_tilavus(self):
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.saldo,self.varasto.tilavuus)

    def test__str__(self):
        tulostus = Varasto(10)
        vastaus = str(tulostus)
        self.assertEqual(vastaus, "saldo = 0, vielä tilaa 10")
        #saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}
    
    def test_tyhja_saldo_sama_kun_tilavus(self):
        self.varasto = Varasto(1,3)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_tyhja_saldo(self):
        self.varasto = Varasto(0,-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_saldo_ja_varasto_yhta_suuri(self):
        self.varasto = Varasto(0)
        self.assertAlmostEqual(self.varasto.tilavuus,0)
    
