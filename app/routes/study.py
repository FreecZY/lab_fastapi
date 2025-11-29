from fastapi import APIRouter
from fastapi.responses import HTMLResponse


router = APIRouter(prefix="/study", tags=["study"])


@router.get("")
async def get_study():
    return HTMLResponse("""
                        Брянский государственный инженерно-технологический университет (БГИТУ) — высшее учебное заведение Брянска. Готовит кадры для лесного хозяйства и лесопромышленного комплекса, для промышленного и гражданского строительства. Выпускает специалистов в области инженерной экологии, ландшафтной архитектуры, государственного и муниципального управления, технологии деревообработки, строительства автомобильных дорог, информационных систем.
                        <br>
                        <img src="https://yandex-images.clstorage.net/g5Eow2148/5e6851J9wy/RnNa0nDGxAz0djcY0mzmAlCBVr0pSGRWoWIm1HfqzcJRqY0A4vKQodf0hP1k7EJKotntnE7iStD2jMvGly6bcwIwUMltn4Bdt3IhCM035EVLzxi8P0R7J5BGE7lPwOumd4y3GPqzxfyX68G5D5xQbvWesug6vS_hqKe00qgAwxByUzCIDNTmD856KieRT_QIFJF_mgNsUgq-Twa5VujxhHmnnwvoqczJn5XQvRS5FHvns5b4P74YxZePreajCtoSRU4UhxzM0T3mZTcvlEDBAC2_VZAhS3gsmUswil_966FBkbUp7Yjl47mV6aEJmQpuwaSS1jelEvqSv5bEiAXfL2R0N5YF4NML03oiJIx00DAMomGCAE52IZpBHZ5W7PS4QL-KM9ip-d2nism4NacDQNOsjuM9vBPFpKK_1pop4DVEQRGUGML8L8ddICSKQOcTKrdakR1sRSyNYwKPacLujGGDrybtuNLftoDYvjWZJkn4n5jDC6Am4a6zvPGaLek_YnUQjCfsxSnoRgwPqGvGPjWOfZoCZmYJnUAbvnvoyKl0t50K6o7y8IGk9Z8RshJi_oyryjOUGNOHrJ7ovRvaKWR0GbUT8OU-xXYoKpZT6DktnEW-OHlxCJxPM512zfWaaIKjF_C-xO2XtuuIILs0Yuiov94QphrFlY2k-4MdzyNsei60PebRDvZ9EC2XauM7NIt_twJLcD-2SzCJeObVi3a3oQLVtOPRqYLKqB2tFEHWo4vGO7I04pCFv8acJtofZ2U4vzfRwS_wbhUpt0jhHB2SXLEkQ2w3gHYqlUTd8r1ijpcY4bPW37-f_Y08ijx9wIWY2i6GK8WBiLrsuQfLDGd6AZsZzPUkxGAoKJVjzRAdv2SXCERrO5hpGrlpzvK5W6CaEOKWy_2srv-DPZoFefCrmfUmkC3xsYOQ7Lcf4BNccyyMC-LRCO1DLQaSdvI8N7ljgDR9bwCqSBaOV-Y">
                        """)
