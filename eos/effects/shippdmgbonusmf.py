# shipPDmgBonusMF
#
# Used by:
# Variations of ship: Rifter (3 of 3)
# Variations of ship: Slasher (3 of 3)
# Ship: Cheetah
# Ship: Freki
# Ship: Republic Fleet Firetail
type = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Projectile Turret"),
                                  "damageMultiplier", ship.getModifiedItemAttr("shipBonusMF"), skill="Minmatar Frigate")
