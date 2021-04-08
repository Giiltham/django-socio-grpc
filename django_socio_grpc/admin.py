from django.contrib import admin
from django_socio_grpc.models import *


class grcpErrorCodeAdmin(admin.ModelAdmin):
	"""

	"""

	list_display = ('code', 'category', 'status', 'notes', 'count', 'created', 'is_active')
	fields = ('code', 'category', 'status', 'notes', 'created',  'is_active', 'is_delete' )
	ordering = ('code', )
	list_filter = ['is_active',  'is_delete', 'category' ]
	list_editable = ['category', ]
	#readonly_fields =  ['xxxxxx',  ]
	search_fields = ['notes', 'status',]



class grcpDataBasesAdmin(admin.ModelAdmin):
	"""

	"""

	list_display = ('service', 'django', 'database', 'description', 'created', 'is_active')
	fields = ('service', 'django', 'database', 'description',  'created',  'is_active', 'is_delete' )
	ordering = ('service', 'database', )
	list_filter = ['is_active',  'is_delete', 'django' ]
	#list_editable = ['category', ]
	#readonly_fields =  ['xxxxxx',  ]
	search_fields = ['django', 'database', 'description',]




class grcpMicroServicesAdmin(admin.ModelAdmin):
	"""

	"""

	list_display = ('service', 'category', 'result', 'isInput', 'count', 'error',  'created', 'is_active')
	fields = ('service', 'directory', 'category', 'description',  'result', 'count', 'error', 'created', 'isInput', 'is_active', 'is_delete' )
	ordering = ('service', )
	list_filter = ['is_active',  'is_delete', 'isInput', 'result' ]
	#list_editable = ['status', ]
	#readonly_fields =  ['xxxxxx',  ]result
	search_fields = ['description', 'service',]
	


class socioGrpcErrorsAdmin(admin.ModelAdmin):
	"""

	"""

	list_display = ('service', 'database', 'error', 'method', 'reason',  'custom',  'created', 'is_active')
	fields = ('service', 'database', 'error', 'reason', 'details', 'custom', 'method', 'aborted', 'query', 'elapse', 'created',  'is_active', 'is_delete' )
	ordering = ('service', )
	list_filter = ['is_active',  'is_delete', 'custom' , 'error' ]
	list_editable = ['custom', ]
	#readonly_fields =  ['xxxxxx',  ]
	search_fields = ['custom', 'details' ]



class grpcLoggingAdmin(admin.ModelAdmin):
	"""
	service      = models.ForeignKey(grcpMicroServices, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Socotec Microservice")    
	database     = models.ForeignKey(grcpDataBases, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Database Microservice")    
	method       = models.IntegerField(default=0, choices=CALL_TYPE)
	query        = models.TextField(default='', null=True, blank=True)
	elapse       = models.FloatField(default=0.00, verbose_name='Elapse Time (sec)')

	"""

	list_display = ('service', 'database', 'method', 'level', 'port', 'elapse', 'error', 'reason', 'message', 'created')
	fields = ('service', 'database', 'method', 'level', 'port', 'elapse', 'error', 'reason', 'message', 'result', 'query',' time', 'created', 'CQRS', 'EventStore', 'is_active', 'is_delete' )
	ordering = ('service', )
	list_filter = ['level', 'is_active',  'is_delete', 'service', 'database', 'method', 'CQRS', 'EventStore', 'error'  ]
	#list_editable = ['custom', ]
	#readonly_fields =  ['xxxxxx',  ]
	#search_fields = ['custom', ]
	
	def error(self):
		from django.utils.html import mark_safe
		if self.error > 0:
			return mark_safe('<span style="color: %s;">%s</span>' % ('red', self.error))
	def reason(self):
		from django.utils.html import mark_safe
		if self.error > 0:
			return mark_safe('<span style="color: %s;">%s</span>' % ('red', self.reason))
	error.allow_tags = True
	error.admin_order_field = 'error'	
	reason.allow_tags = True
	reason.admin_order_field = 'reason'	



class SpecialLogAdmin(admin.ModelAdmin):
	"""
	time = models.DateTimeField(auto_now_add=True)
	level = models.CharField(max_length=10)
	message = models.TextField()

	"""

	list_display = ('time', 'level', 'message', 'created')
	fields = ('time', 'level', 'message', 'created',  )
	ordering = ('level', )
	list_filter = ['level',  ]

	

class grcpProtoBufAdmin(admin.ModelAdmin):
	"""

	"""

	list_display = ('protobuf', 'service', 'created', 'is_active')
	fields = ('protobuf', 'file', 'service', 'created',  'is_active', 'is_delete' )
	ordering = ('protobuf', )
	list_filter = ['is_active',  'is_delete', ]
	#list_editable = ['status', ]
	#readonly_fields =  ['xxxxxx',  ]
	#search_fields = ['description', 'service',]



class grcpProtoBufFieldsAdmin(admin.ModelAdmin):
	"""

	"""

	list_display = ('database', 'protobuf', 'field', 'is_query', 'is_update', 'created', 'is_active')
	fields = ('database', 'protobuf', 'field',  'field_sequence', 'query_sequence', 'created', 'is_query', 'is_update',  'is_active', 'is_delete' )
	ordering = ('protobuf', )
	list_filter = ['is_active',  'is_delete', 'is_query', 'is_update' ]
	list_editable = ['is_update', 'is_query' ]
	#readonly_fields =  ['xxxxxx',  ]
	#search_fields = ['description', 'service',]



class grpcMethodAdmin(admin.ModelAdmin):
	"""

	"""

	list_display = ('service', 'database', 'method', 'result', 'input', 'is_update', 'is_active')
	fields = ('service', 'database', 'method', 'result', 'input', 'is_update', 'is_active', 'is_delete' )
	ordering = ('service', 'database' )
	list_filter = ['is_active',  'is_delete', 'is_update', 'method', 'result', 'input' ]
	#list_editable = ['status', ]
	#readonly_fields =  ['xxxxxx',  ]
	#search_fields = ['description', 'service',]

	
	
admin.site.register(grcpErrorCode, grcpErrorCodeAdmin)	
admin.site.register(grcpMicroServices, grcpMicroServicesAdmin)	
admin.site.register(grcpDataBases, grcpDataBasesAdmin)	
admin.site.register(socioGrpcErrors, socioGrpcErrorsAdmin)	
admin.site.register(grcpProtoBuf, grcpProtoBufAdmin)	
admin.site.register(grcpProtoBufFields, grcpProtoBufFieldsAdmin)	
admin.site.register(grpcLogging, grpcLoggingAdmin)	
admin.site.register(grpcMethod, grpcMethodAdmin)	
admin.site.register(SpecialLog, SpecialLogAdmin)	





	

