# ewSkillTdFallOffBonus
#
# Used by:
# Skill: Frequency Modulation
type = "passive"


def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Weapon Disruptor",
                                  "falloffEffectiveness", skill.getModifiedItemAttr("falloffBonus") * skill.level)
