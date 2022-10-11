from .base import Skill


class FuryPunch(Skill):
    name = "Свирепый пинок"
    stamina = 6
    damage = 12

    def skill_effect(self) -> str:
        """ Расчет нанесенного урона умения, и расхода выносливости противника """

        self.target.get_damage(self.damage)
        self.user.stamina -= self.stamina

        return f'{self.user.name} использует {self.name} и наносит {self.damage} урона сопернику.'

