pushd ..

	git clone https://github.com/richardghirst/PiBits.git pibits
	
	pushd pibits/ServoBlaster/user

		make servod

	popd

popd
