## Py Transforms for Image Similarity

def filter_out_similarity(near_dup_ids):
	"Return true if there are too many ids"
	if near_dup_ids == '' or near_dup_ids.count(',') > 100 :
		return "1"
	else:
		return "0"


def similar_image_uri(img_id, filter_out):
	"Return the URI of a similar image, empty if filter_out"
	if filter_out == '1':
		return ''
	else:
		return "image/" + getValue("similar_image_ids_Values")


def similar_image_score(distance, filter_out):
	"return the score as a float string, empty if filter_out"
	if filter_out == '1':
		return ''
	else:
		return '{0:.15f}'.format(float(distance))


def similar_image_role_uri(ad_id, img_id, sim_id, filter_out):
	"Return the URI of the role for similar images, empty if filter_out"
	if filter_out == '1':
		return ''
	else:
		return uri_from_fields("role/",ad_id, img_id, sim_id)
		
