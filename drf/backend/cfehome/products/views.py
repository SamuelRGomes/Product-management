from rest_framework import  generics,mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404 

from api.mixins import StaffEditorPermissionMixin,UserQuerySetMixin
from .models import Product
 
from .serializers import ProductSerializer
class ProductListCreateAPIView(UserQuerySetMixin,StaffEditorPermissionMixin,generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
 
    def perform_create(self,serializer):
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=title
        serializer.save(user=self.request.user,content=content)
    
    # def get_queryset(self, *args, **kwargs):
    #     qs=super().get_queryset(*args, **kwargs)
    #     request=self.request
    #     user=request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     return qs.filter(user=request.user)
    
product_list_create_view = ProductListCreateAPIView.as_view()
class ProductDetailApiView(UserQuerySetMixin,StaffEditorPermissionMixin,generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
   
product_detail_view = ProductDetailApiView.as_view()   
class ProductUpdateApiView(UserQuerySetMixin,StaffEditorPermissionMixin,generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'
   

    def perform_update(self,serializer):
        instance=serializer.save()
        if not instance.content:
            instance.content=instance.title
product_update_view = ProductUpdateApiView.as_view()  
class ProductDeleteApiView(UserQuerySetMixin,StaffEditorPermissionMixin,generics.DestroyAPIView):
  queryset=Product.objects.all()
  serializer_class=ProductSerializer
  lookup_field='pk'
 
  def perform_delete(self,instance):
    super().perform_destroy(instance) 
product_delete_view = ProductDeleteApiView.as_view()
class ProductMixinView(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'
    def get(self, request, *args, **kwargs):
        pk=kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def perform_create(self,serializer):
        print(serializer.validated_data)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=title
        serializer.save(content=content)
product_mixin_view = ProductMixinView.as_view()

# class ProductListApiView(generics.RetrieveAPIView):
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer
# product_list_view = ProductListApiView.as_view()
@api_view(['GET', 'POST'])
def product_alt_view(request,pk=None, *args, **kwargs):
    method=request.method 
    if method=='GET':
        if pk is not None:
            obj=get_object_or_404(Product,pk=pk)
            data=ProductSerializer(obj,many=False).data
            return Response(data)

        queryset=Product.objects.all()
        data=ProductSerializer(queryset,many=True).data
        return Response(data)
    if method=='POST':
        serializer=ProductSerializer(data=request.data)
    if serializer.is_valid():
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=title
        serializer.save(content=content)    
        print(serializer.data)
        return Response(serializer.data)   
    return Response({'invalid':'not good data'},status=400)

