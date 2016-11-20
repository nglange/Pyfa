# subsystemBonusCaldariOffensive3EwStrengthRadar
#
# Used by:
# Subsystem: Tengu Offensive - Rifling Launcher Pattern
type = "passive"


def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "ECM",
                                  "scanRadarStrengthBonus",
                                  module.getModifiedItemAttr("subsystemBonusCaldariOffensive3"),
                                  skill="Caldari Offensive Systems")
