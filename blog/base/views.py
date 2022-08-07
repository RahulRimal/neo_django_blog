from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    # return HttpResponse('This is a home page')
    blog_info = [
        {
            'id': 1,
            'title': 'Django is fun to learn',
            'desc': 'Django is extremely fast, secure and reliable web framework which helps us to build scalable web app very fast'
        },
        {
            'id': 2,
            'title': "Lorem Ipsum as dummy text",
            'desc': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Ad quod soluta doloremque doloribus qui reprehenderit fugiat nesciunt quam. Aliquid rerum animi modi ad, aspernatur deleniti cum facere, sint distinctio explicabo voluptates repellendus voluptatem sapiente eius facilis recusandae ipsam delectus reiciendis! Ad consectetur praesentium architecto deleniti quidem neque repudiandae aliquam ea pariatur placeat consequatur distinctio, eius libero? Inventore quos unde reprehenderit recusandae, consequatur commodi sit ipsa nihil quidem adipisci earum sed rerum ea voluptas architecto natus doloremque saepe nulla iure perspiciatis hic praesentium itaque. Quasi quisquam dignissimos ex sit? Non illo dolore praesentium! Atque in animi tempore modi. Voluptate sint nobis non blanditiis accusantium expedita, nihil cupiditate et qui ipsa nisi voluptatibus ea, libero fugiat. Obcaecati porro quis ad impedit eveniet cupiditate deleniti minus deserunt nostrum fugit, modi suscipit reiciendis omnis inventore veniam quidem iure hic, eaque necessitatibus eos quisquam ea, iste voluptatum provident. Neque id aut eaque porro voluptate odit eligendi laboriosam velit nulla qui numquam, hic dolor suscipit iure in tempora mollitia eius modi perferendis sequi optio officiis! Ex a voluptatibus doloremque laboriosam aut deleniti nostrum molestiae, sunt itaque perferendis doloribus ratione nobis voluptates sed accusamus blanditiis odit non illum maiores. Doloremque laboriosam eaque itaque harum consectetur? Possimus, ullam?'
        }
    ]
    return  render(request, 'home.html', {'blog_info': blog_info})

def post(request):
    return HttpResponse('This is a post page')