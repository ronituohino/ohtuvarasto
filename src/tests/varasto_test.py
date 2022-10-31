import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    # perustoiminnallisuus

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

    def test_str_esitys(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
        self.varasto.lisaa_varastoon(5)
        self.assertEqual(str(self.varasto), "saldo = 5, vielä tilaa 5")
        self.varasto.ota_varastosta(3)
        self.assertEqual(str(self.varasto), "saldo = 2, vielä tilaa 8")

    # virheellinen käyttö

    def test_konstruktori_neg_tilavuus_nollataan(self):
        self.testVarasto = Varasto(-1)
        self.assertAlmostEqual(self.testVarasto.tilavuus, 0)

    def test_konstruktori_neg_saldo_nollataan(self):
        self.testVarasto = Varasto(10, -1)
        self.assertAlmostEqual(self.testVarasto.saldo, 0)

    def test_lisays_neg_maara_sivuutetaan(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_ottaminen_neg_maara_sivuutetaan(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    # ylimäärät

    def test_konstruktori_ylimaarainen_saldo_hukkaan(self):
        self.testVarasto = Varasto(10, 20)
        self.assertAlmostEqual(self.testVarasto.saldo, 10)

    def test_lisays_ylimaara_hukkaan(self):
        self.varasto.lisaa_varastoon(13)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_ylimaara_sivuutetaan(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(7)
        self.assertAlmostEqual(self.varasto.saldo, 0)
