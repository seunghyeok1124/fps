from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# 플레이어 설정 (WASD 이동 및 마우스 시점 전환 자동 지원)
player = FirstPersonController()
player.y = 2  # 플레이어 시작 높이

# 기본 바닥 생성
ground = Entity(
    model='plane',
    scale=(100, 1, 100),
    color=color.lime,
    texture='white_cube',
    collider='box'
)

# 간단한 벽/건물 구조물 (어센트 맵 형태의 지형으로 확장 가능)
wall = Entity(
    model='cube',
    scale=(10, 5, 2),
    position=(0, 2.5, 10),
    color=color.gray,
    collider='box'
)

# 총 모형 생성
gun = Entity(
    model='cube',
    parent=camera.ui,
    scale=(0.2, 0.1, 0.5),
    position=(0.5, -0.4, 0.8),
    color=color.dark_gray
)

# 마우스 클릭 이벤트 (총 쏘기)
def input(key):
    if key == 'left mouse down':
        # 총알 발사 연출 (레이캐스트를 통해 조준선 위치의 물체 감지)
        bullet_ray = raycast(camera.world_position, camera.forward, distance=100)
        if bullet_ray.hit:
            # 총알이 맞은 위치에 간단한 흔적 남기기
            bullet_mark = Entity(
                model='sphere',
                color=color.red,
                scale=0.2,
                position=bullet_ray.world_point
            )
            destroy(bullet_mark, delay=2)  # 2초 후 삭제

app.run()
